import React, { Component } from 'react';
import { Button, Card, CardImg, CardText, CardBody, CardTitle, CardSubtitle } from 'react-bootstrap';
import '../styles/App.css';
import ReactModal from 'react-modal';



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

  handleOpenModal () {
    this.setState({ showModal: true });
  }

  handleCloseModal () {
    this.setState({ showModal: false });
  }

  render() {
    return (

      <div className="home-page">
        <div className="profile__container">
            <img className="circular_image" src="https://i.pinimg.com/564x/7f/39/29/7f3929dd34913078c4c9db9ead3e5df5.jpg" />
            <h1> @frankMurray </h1>
            <Button disabled bsStyle="primary" className="profile_button">
              Frank Muurray
            </Button>

            <br />
            <br />

            <Button bsStyle="primary" className="signup_button" onClick={this.login.bind(this)}>
              Change Password
            </Button>

            <br />
            <br />

            <Button bsStyle="primary" className="signup_button">
              Add a new class
            </Button>
        </div>

        <div>
          <button onClick={this.handleOpenModal}>Trigger Modal</button>
          <ReactModal isOpen={this.state.showModal} contentLabel="Minimal Modal Example">
            <form>
              <label>
                Courses:
                <input type="text" name="Courses" />
              </label>
              <input type="submit" value="Submit" />
            </form>
            <button onClick={this.handleCloseModal}>Close Modal</button>
          </ReactModal>
        </div>

      </div>
    );
  }
}



export default Profile;
