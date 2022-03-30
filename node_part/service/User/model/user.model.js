const request = require("request");
const ejs = require("ejs");
const axios = require("axios");

//---------- Get All Users -------------//

const getAllUsersData = (req, res) => {
  request("http://127.0.0.1:5000/users", function (error, response, body) {
    console.log("statusCode:", response.body); // Print the response status code if a response was received
    let resBody = JSON.parse(response.body);
    console.log(typeof resBody);
    res.render("dashboard", { resBody }); //Display the response on the website
  });
  // res.send({ success: true, message: DATA_AVAILABLE, data: Data });
};

const AddUserDataPage = (req, res) => {
  res.render("addUser"); //Display the response on the website
};

const AddUserData = (req, res) => {
  // console.log("haresh-----------", req.body);
  axios
    .post("http://localhost:5000/add/data", req.body)
    .then((resBody) => {
      console.log(resBody);
      res.redirect("/user");
    })
    .catch((error) => {
      console.log(error);
    });
};

const getUserData = async (req, res) => {
  const id = req.params.id;

  axios
    .get(`http://localhost:5000/users/${id}`)
    .then((response) => {
      // let resBody = JSON.parse(response.body);
      // console.log(typeof resBody);
      // res.render("addUser", { resBody });
      response = response.data;
      console.log(response);
      res.render("UpdateUser", { response });
    })
    .catch((error) => {
      console.log(error);
    });
};

const UpdateUserData = async (req, res) => {
  const id = req.params.id;
  console.log("hussain---------", id);
  axios
    .post(`http://localhost:5000/users/update/${id}`, req.body)
    .then((response) => {
      console.log(response);
      res.redirect("/user");
    })
    .catch((error) => {
      console.log(error);
    });
};

const getOneUsersData = async (req, res) => {
  const id = req.params.id;
  console.log("hussain---------", id);

  axios
    .get(`http://localhost:5000/users/${id}`)
    .then((response) => {
      let resBody = response.data;
      res.render("UserPage", { resBody });
    })
    .catch((error) => {
      console.log(error);
    });
};

const DeleteUserData = async (req, res) => {
  const id = req.params.id;
  console.log("Delete id:-----------------", id);
  axios
    .post(`http://localhost:5000/users/delete/${id}`)
    .then((response) => {
      console.log(response);
      res.render("/user");
    })
    .catch((error) => {
      console.log(error);
    });
};

module.exports = {
  getAllUsersData,
  AddUserDataPage,
  DeleteUserData,
  AddUserData,
  UpdateUserData,
  getUserData,
  getOneUsersData,
  // DeleteUserDataPage,
};
