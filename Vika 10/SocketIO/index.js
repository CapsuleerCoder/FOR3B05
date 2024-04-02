import express from 'express';
import { createServer } from 'node:http';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { Server } from 'socket.io';

const app = express("public");
const server = createServer(app);
const io = new Server(server);

let activeUsers = []
let guestCount = 0;

const __dirname = dirname(fileURLToPath(import.meta.url));

app.use(express.static(join(__dirname, '')));

app.get('/', (req, res) => {
  res.sendFile(join(__dirname, 'index.html'));
});

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

    socket.on("chat message", (msg) => {
        io.emit('chat message', msg);
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

    guestCount = io.engine.clientsCount - activeUsers.length;
    io.emit("update guest count", guestCount);
  });

server.listen(3000, () => {
  console.log('server running at http://localhost:3000');
});