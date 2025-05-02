const { request } = require('express');
var express = require('express');
const { PythonShell } = require('python-shell');
var router = express.Router();

/* GET users listing. */
router.get('/', async function(req, res, next) {

    // let py = new PythonShell("./pythonScripts/jobScraper.py")
    // let jobs = ""
    // let currentJob = []

    // py.on("message", (message) => {
    //     jobs = message
    // })
    
    // py.end((err, code, signal) => {
    //     if(err) throw err;

    //     console.log(jobs)
    //     res.render('scrapeList',{title : "Jobs from Slotech",jobs : JSON.parse(jobs)});
    //     console.log('The exit code was: ' + code);
    //     console.log('The exit signal was: ' + signal);
    //     console.log('finished');
    // })
    mojeDeloResponse = await fetch("https://slo-tech.com/delo");

    console.log(mojeDeloResponse.body);

    res.send(mojeDeloResponse.body);
});

module.exports = router;