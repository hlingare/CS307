import React, { Component } from 'react';
import { Navbar, Button, Jumbotron } from 'react-bootstrap';
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
      <div>

      <Jumbotron>
        <h1 className="display-3">CourseRec</h1>
        <p className="lead">CourseRec is an app that allows students to find course which best suits them.</p>
      </Jumbotron>




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
      </div>
    );
  }
}

export default App;
