import express from 'express';  //importar express "middlewareið"
import { createServer } from 'node:http'; // importar function sem gerir server
import { fileURLToPath } from 'node:url'; //breytir file URL í file path.
import { dirname, join } from 'node:path';  // dirname og join functions
import { Server } from 'socket.io';     // Þetta er class, sem sem gerir server.

const app = express("public");      // gerir breytu sem heitir app sem er að notast við þetta express middleware
const server = createServer(app);   // gerir server breytu með app breytunni
const io = new Server(server);      // Gerir nýja breytu með nújum klasa af server

let activeUsers = []    //listi yfir user names
let guestCount = 0;     //teljari fyrir guest count. 

const __dirname = dirname(fileURLToPath(import.meta.url));  // breyta sem segir hvernig þú kemst í gögn sem notuð eru.

app.use(express.static(join(__dirname, '')));   // segir "app" að nota breytu fyrir ofan til að komast í css skjalið.

app.get('/', (req, res) => {      // request er client að biðja server, response er server að svara          
  res.sendFile(join(__dirname, 'index.html'));
});  // client/req að tala við server/res, þegar kallað er í hann er sent _dirname/index.html

io.on("connection", (socket) => {
    console.log('a user connected');
    let typingTimer;

    socket.emit("update users", activeUsers);
    socket.emit("update guest count", guestCount);

    socket.on("disconnect", () => {
      console.log('user disconnected');
      const disconnectedUser = activeUsers.find(user => user.id === socket.id);
      if (disconnectedUser) {
        activeUsers = activeUsers.filter(user => user.id !== socket.id);
        io.emit('update users', activeUsers);
      }
      guestCount = io.engine.clientsCount - activeUsers.length;
      io.emit("update guest count", guestCount);
    });

      socket.on("join room", (room) => {
        socket.join(room);
        socket.room = room;
    });
    
    socket.on("leave room", (room) => {
        socket.leave(room);
        socket.room = null; 
    });

    socket.on("set user", (username) => {
      const existingUser = activeUsers.find(user => user.id === socket.id);
      if (!existingUser) {
        activeUsers.push({ id: socket.id, username });
        io.emit("update users", activeUsers);
      }
      guestCount = io.engine.clientsCount - activeUsers.length;
      io.emit("update guest count", guestCount);
    });

    socket.on("typing", (username) => 
    {
      clearTimeout(typingTimer)
      socket.broadcast.emit("user typing", username)
    });

    socket.on("stop typing", () => 
    {
      typingTimer = setTimeout(() =>
      {
        socket.broadcast.emit("stop typing")
      }, 2000)
    })

    socket.on("chat message", (msg) => {
          io.to(socket.room).emit('chat message', msg);
  });

    guestCount = io.engine.clientsCount - activeUsers.length;
    io.emit("update guest count", guestCount);
  });

server.listen(3000, () => {
  console.log('server running at http://localhost:3000');
});