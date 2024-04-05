// joi er forritasafn (module) sem leyfir okkur að prófa gögnin sem við tökum við frá notanda
// athugið að til að keyra þessa skrá þarf augljóslega fyrst að hlaða niður bæði express og joi
// með npm 
// en með skipuninni: npm install 
// má fá alla pakka ef package.json skráin fylgir með
const Joi = require('joi');
const express = require('express');
const app = express();

// express.json er innbyggt "middleware" í express, það leyfir okkur að vinna með body objectið í 
// beiðni (req.body) ef það er á JSON (JavaScript Object Notation) formi  en JSON er ákveðinn 
// gagnastandard sem er mikið notaður m.a. með nodejs
app.use(express.json());

const projects = [
	{ id: 1, name: 'verkefni1'},
	{ id: 2, name: 'verkefni2'},
	{ id: 3, name: 'verkefni3'}
];

// () => {} syntaxinn þýðir að við erum að skrifa svokallað "lambda" fall 
// (stundum líka kallað "arrow" eða "fat-arrow" fall)
app.get('/', (req, res) => {
	res.send('Hello world');
});

// hér skrifum við rútu fyrir verkefnin okkar ef fólk vill sjá þau
app.get('/projects', (req, res) => {
	res.send(projects);
});

// rúta sem leyfir notanda að tilgreina aðeins eitt verkefni, id er hér parameter
app.get('/projects/:id', (req, res) => {
	// ágætis umfjöllun um array find aðferðina í javascript: 
	// https://www.w3schools.com/jsref/jsref_find.asp
	// en hér notum við hana til að finna það stak í projects fylkinu sem við ætlum
	// að skila notanda
	const project = projects.find((p) => {
		if (p.id === parseInt(req.params.id)) {
			return p;
		}
	});
	// einnig hefði mátt gera venjulegt fall í staðinn 	
	// en það er sýnt hér að neðan
	// const project = projects.find(function(p) {
	// 	if (p.id === parseInt(req.params.id)) {
	// 		return p;
	// 	}
	// });
	// ef verkefni með þetta id fannst ekki þá sendum við villuskilaboð
	// og endum fallið okkar með return
	if (!project) {
		res.status(404).send('The project with the given ID was not found!');
		return;
	}
	// annars sendum við notanda rétta verkefnið
	res.send(project);
});

// hér er post rúta með gagnaskoðun (data validation)
// við búumst hér við að í req.body sé JSON object
// ATHUGIÐ að hér er gert ráð fyrir notkun Postman forritsins til að senda beiðnina
app.post('/projects', (req, res) => {	
	// köllum á fallið verkefnisCheck til að athuga hvort allt sé í lagi
	const niðurstaða = verkefnisCheck(req.body);
	if (niðurstaða.error) {
		// ef gögn eru ógild þá sendum við 400 status til baka
		res.status(400).send(niðurstaða.error.details[0].message);
		return;
	}
	// ef allt er í lagi, þá höldum við áfram sem fyrr
	
	// fyrst gerum við nýjan object sem er svipaður þeim sem við höfum í projects
	// fylkinu okkar, en nú fáum við name breytuna frá JSON objectnum sem notandi 
	// sendir okkur
	var project = {
		id: projects.length + 1,
		name: req.body.name
	};
	// bætum svo hlutnum við fylkið okkar (en athugið að þar sem við erum ekki
	// með neinn gagnagrunn, þá hverfur nýja verkefnið auðvitað þegar við drepum serverinn)
	projects.push(project);
	res.send(project);
});

// fall til að framkvæma gagnaskoðun og ganga úr skugga um að verkefnið samræmist 
// reglum okkar um hvernig verkefni á að líta út
function verkefnisCheck(verkefni) {
	// segjum fyrst til um hvaða shcema við viljum nota, þ.e.a.s. hvaða reglur 
	// við viljum hafa um verkefnis objectana okkar
	const schema = Joi.object({
		// breytan nafn verður að vera strengur með minnst 3 stafi
		name: Joi.string().min(3).required()
	});
	return schema.validate(verkefni);
}

// environment breytuna má stilla með skipunum (í skipanalínu):
// á pc er það set PORT=x, t.d. set PORT=5000 til að 
// fá port 5000
// á mac er það export PORT=x,, t.d. set PORT=5000 til að 
// fá port 5000
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening on port ${port}...`));


