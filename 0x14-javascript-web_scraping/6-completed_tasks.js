#!/usr/bin/node

// This script computes the number of tasks completed by user id.
//  The first argument is the API URL
//  Only print users with completed task
const request = require('request');

// const ApiUrl = 'https://jsonplaceholder.typicode.com/todos'

request(process.argv[2], function(err, _response, body){
    if (err){
        console.log(response)
    } else{
        usersCompletedTasks = {};
        body = JSON.parse(body)

        for(let i = 0; i < body.length; i++){
            const userId = body[i].userId;
            const completed = body[i].completed;

            if (completed && !usersCompletedTasks[userId]){
                usersCompletedTasks[userId] = 0;
            }

            if (completed) ++usersCompletedTasks[userId];
        }
        console.log(usersCompletedTasks);
    }
})
