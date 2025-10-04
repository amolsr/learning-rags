### create middleware name logger.js (or whatever you please). copy the following code below
```
const expressWinston = require('express-winston');

const requestLog = expressWinston.logger({
  transports: [
    new winston.transports.Console({
      format: winston.format.json({
        space: 2
      })
    }),
    new winston.transports.MongoDB({
      db: 'localhost:27001', //Your Db connection
      options: {
        useNewUrlParser: true,
        poolSize: 2,
        autoReconnect: true
      }
    })
  ],
  meta: true,
  msg: "Request: HTTP {{req.method}} {{req.url}}; Username: {{req.user.preferred_username}}; ipAddress {{req.connection.remoteAddress}}",
  requestWhitelist: [
    "url",
    "method",
    "httpVersion",
    "originalUrl",
    "query",
    "body"
  ]
});

exports.requestLog = requestLog;
```

### In your app.js file, require the logger file so that is applied globally:

```
const logger = require('../middleware/logger');
const express = require('express');
const app = express();

app.use(logger.requestLog);
```
