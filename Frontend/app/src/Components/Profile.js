import React, { Component } from 'react';
import { Button, Card, CardImg, CardText, CardBody, CardTitle, CardSubtitle } from 'react-bootstrap';
import '../styles/App.css';
import ReactModal from 'react-modal';
import { postCourseData } from '../utils/api';
import { postUserName } from '../utils/api';
import { getUserData } from '../utils/api';
import DropzoneS3Uploader from 'react-dropzone-s3-uploader'


class Profile extends Component {


  handlePrint() {
    if (this.state.value) {
      console.log(this.state.value);
    }
  }
  handleFinishedUpload = info => {
    console.log("hazard");
     console.log('File uploaded with filename', info.filename)
     console.log('Access it on s3 at', info.fileUrl)
  }

  handleChange(e) {
    this.setState({ value: e.target.value });
  }

  login() {
    this.props.auth.login();
  }

  constructor () {
    super();
    this.state = {
      showModal: false,
      username: ""
    };

    this.state = {value: '12'};
    this.handleUserChange = this.handleUserChange.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleOpenModal = this.handleOpenModal.bind(this);
    this.handleCloseModal = this.handleCloseModal.bind(this);
  }
  componentWillUnmount(){
    //make api post
    var uid = window.localStorage.getItem("uid");
    postUserName(uid,this.state.username)
  }




  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleUserChange(event) {
    this.setState({username: event.target.value});
  }

  handleSubmit(event) {

    if (document.getElementById('FileName').value==""|| document.getElementById('FileName').value==undefined)
    {
        alert("Please Enter a Course Name");
        return false;
    }
    var uid = window.localStorage.getItem("uid");
    postCourseData(uid,document.getElementById('FileName').value,this.state.value)
    alert("Course "+document.getElementById('FileName').value+" has been added!! " + this.state.value);
    return true;
    event.preventDefault();
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


  render() {
    const uploadOptions = {
      server: 'http://localhost:4000',
      signingUrlQueryParams: {uploadType: 'avatar'},
}
  const s3Url = 'https://my-bucket.s3.amazonaws.com'
    return (
      <div className="home-page">
        <div className="profile__container">
            <br />
            <br />
            <img  className="circular_image" src="https://static-cdn.jtvnw.net/jtv_user_pictures/barneezyjones-profile_image-fac2b2f47d17661b-300x300.png" />
            <br />
            <center>
            <input
            type="text"
            className="signup_button"
            value ={this.state.username}
            onChange = {this.handleUserChange}
            />
            </center>
            <br />

            <Button bsStyle="primary" className="signup_button">
            {this.state.username}
            </Button>

            <br/>
            <Button bsStyle="primary" className="signup_button" onClick={this.login.bind(this)}>
              Change Password
            </Button>
              <DropzoneS3Uploader
                onFinish={this.handleFinishedUpload}
                s3Url={s3Url}
                maxSize={1024 * 1024 * 5}
                upload={uploadOptions}
       />
            <br/>
            <form name="frm1" id="frm1" className="signup_button">
              <p>Add Courses you Have Taken</p>
              <input type="text" name="FileName" id="FileName" />
              <br/>
              <br/>
              <p>Performance Rating</p>
              <select value={this.state.value} onChange={this.handleChange}>
                <option value="13">Good</option>
                <option value="12">Okay</option>
                <option value="11">Bad</option>
              </select>
              <br/>



              <Button onClick={this.handleSubmit.bind(this)}>
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
