const express = require("express");
const path = require("path");
const User = require("./service/User/router");
const app = express();
const bodyParser = require("body-parser");
require("dotenv").config();

/* This parses the JSON from the AJAX req */
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
// set view folder & ejs
console.log(__dirname);
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.use("/user", User);

app.listen(process.env.PORT, () => {
  console.log(`You are live on ${process.env.PORT}............`);
});
