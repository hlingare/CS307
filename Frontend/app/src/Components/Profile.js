import React, { Component } from 'react';
import { Button, Card, CardImg, CardText, CardBody, CardTitle, CardSubtitle } from 'react-bootstrap';
import '../styles/App.css';
import ReactModal from 'react-modal';
import AlertContainer from 'react-alert'



class Profile extends Component {


  login() {
    this.props.auth.login();
  }

  constructor () {
    super();
    this.state = {
      showModal: false
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
          alert("Please Enter a File Name");
          return false;
      }
      alert("Course has Been Added");
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
              Frank Muurray
            </Button>
            <br/>









            <form name="frm1" id="frm1" className="signup_button" >
              <p>Add Courses you Have Taken</p>
              <input type="text" name="FileName" id="FileName"/>
              <input type="submit" value="send" name="btn_move" id="btn_move" onClick={this.checkCourse}/>
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
