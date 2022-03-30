const router = require("express").Router();
const models = require("./model/user.model");
const axios = require("axios");

router.get("/", models.getAllUsersData);
router.get("/:id", models.getOneUsersData); //Get user by id in page
router.get("/add/new", models.AddUserDataPage); //Add User page
router.post("/add/new", models.AddUserData); //Add User

// Update
router.get("/update/:id", models.getUserData); //Rendering Page
router.post("/update/:id", models.UpdateUserData);

//Delete
// router.get("/delete/:id", models.DeleteUserDataPage);
router.post("/delete/:id", models.DeleteUserData);

router.get("*", (req, res) => {
  res.status(404).render("error");
});
module.exports = router;
