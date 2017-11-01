import React, { Component } from 'react';
import { Button, Card, CardImg, CardText, CardBody, CardTitle, CardSubtitle } from 'react-bootstrap';
import '../styles/App.css';
import ReactModal from 'react-modal';
import AlertContainer from 'react-alert'
import { postCourseData } from '../utils/api';
import { getUserData } from '../utils/api';



class Profile extends Component {


  login() {
    this.props.auth.login();
  }

  constructor () {
    super();
    this.state = {
      showModal: false,
      username: ""
    };

    this.handleOpenModal = this.handleOpenModal.bind(this);
    this.handleCloseModal = this.handleCloseModal.bind(this);
  }

  sendEmail(message) {
    var email = message.emailId;
    var subject = message.subject;
    var emailBody = 'Hi '+message.from;
    document.location = "mailto:"+email+"?subject="+subject+"&body="+emailBody;
  }
  getUserData() {
  getUserData().then((username) => {
    this.setState({username: username.result.username});
  });
}

componentDidMount() {
  this.getUserData();
}

  handleOpenModal () {
    this.setState({ showModal: true });
  }

  handleCloseModal () {
    this.setState({ showModal: false });
  }

  showAlert() {
    alert("Course Was Added");
  }

  checkCourse()
  {
      if (document.getElementById('FileName').value==""|| document.getElementById('FileName').value==undefined)
      {
          alert("Please Enter a Course Name");
          return false;
      }
      var uid = window.localStorage.getItem("uid");
      postCourseData(uid,document.getElementById('FileName').value)
      alert("Course "+document.getElementById('FileName').value+" has been added!!");
      return true;
  }

  render() {
    return (
      <div className="home-page">
        <div className="profile__container">
            <br />
            <br />
            <img className="circular_image" src="https://static-cdn.jtvnw.net/jtv_user_pictures/barneezyjones-profile_image-fac2b2f47d17661b-300x300.png" />

            <center><h1> @frankMurray </h1></center>

            <Button bsStyle="primary" className="signup_button">
            {console.log(this.state,"state")}
            {this.state.username}
            </Button>

            <br/>
            <Button bsStyle="primary" className="signup_button" onClick={this.login.bind(this)}>
              Change Password
            </Button>
            <br/>

            <form name="frm1" id="frm1" className="signup_button">
              <p>Add Courses you Have Taken</p>
              <input type="text" name="FileName" id="FileName" />
              <br/>
              <Button onClick={this.checkCourse.bind(this)}>
                Submit
              </Button>
            </form>
            <center>
            <a className = "App" href="mailto:someone@yoursite.com?subject=Mail from Our Site">Email Us if you are having trouble with the app.</a>
            </center>
        </div>
      </div>
    );
  }
}
export default Profile;