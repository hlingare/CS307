import React, { Component } from 'react';
import { Navbar, Button, Jumbotron, NavItem, NavLink } from 'react-bootstrap';
import './styles/App.css';

class App extends Component {
  goTo(route) {
    this.props.history.replace(`/`)
  }

  login() {
    this.props.auth.login();
  }

  logout() {
    this.props.auth.logout();
  }

  render() {
    const { isAuthenticated } = this.props.auth;

    return (
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
              className="signup_button"
              onClick={this.login.bind(this)}
            >
            Sign Up
            </Button>
          )
      }
        </div>
      </div>
    );
  }
}

export default App;
