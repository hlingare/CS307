import React, { Component } from 'react';
import logo from './logo.svg';
import './styles/App.css';
import Auth from './utils/AuthService.js';
const auth = new Auth();

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to Course Rec </h2>
          {  auth.login()}
        </div>
      </div>
    );
  }
}

export default App;
