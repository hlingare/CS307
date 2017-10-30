import React, { Component } from 'react';
<<<<<<< HEAD
import { Navbar, Button, Jumbotron, NavItem, NavLink } from 'react-bootstrap';
import './styles/App.css';

class App extends Component {
=======
import { Navbar, Button } from 'react-bootstrap';
import './styles/App.css';

class App extends Component {
  goTo(route) {
    this.props.history.replace(`/`)
  }
>>>>>>> c9d69db426ac4532f4d8edbc6797f95a7aad8196

  login() {
    this.props.auth.login();
  }

<<<<<<< HEAD
=======
  logout() {
    this.props.auth.logout();
  }

>>>>>>> c9d69db426ac4532f4d8edbc6797f95a7aad8196
  render() {
    const { isAuthenticated } = this.props.auth;

    return (
<<<<<<< HEAD
      <div className="home-page">
        <div className="home-page__container">
        <h1> CourseRec </h1>

      {
        !isAuthenticated() && (
            <Button

              bsStyle="primary"
              className="login_button"
              onClick={this.login.bind(this)}
            >
              Log In
            </Button>
          )
      }
      {
        !isAuthenticated() && (
            <Button
              bsStyle="primary"
              className="hmsignup_button"
              onClick={this.login.bind(this)}
            >
            Sign Up
            </Button>
          )
      }
        </div>
=======
      <div>
        <Navbar fluid>
          <Navbar.Header>
            <Navbar.Brand>
              <a href="#">Course Rec</a>
            </Navbar.Brand>
            <Button
              bsStyle="primary"
              className="btn-margin"
              onClick={this.goTo.bind(this, 'Courses')}
            >
              Home
            </Button>
            {
              !isAuthenticated() && (
                  <Button
                    bsStyle="primary"
                    className="btn-margin"
                    onClick={this.login.bind(this)}
                  >
                    Log In
                  </Button>
                )
            }
            {
              !isAuthenticated() && (
                  <Button
                    bsStyle="primary"
                    className="btn-margin"
                    onClick={this.login.bind(this)}
                  >
                  Sign Up
                  </Button>
                )
            }
            {
              isAuthenticated() && (
                  <Button
                    bsStyle="primary"
                    className="btn-margin"
                    onClick={this.logout.bind(this)}
                  >
                    Log Out
                  </Button>
                )
            }
          </Navbar.Header>
        </Navbar>
>>>>>>> c9d69db426ac4532f4d8edbc6797f95a7aad8196
      </div>
    );
  }
}

export default App;
