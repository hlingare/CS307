import React, { Component } from 'react';
import { Link } from 'react-router-dom'

class Nav extends Component {

  render() {
    return (
        <ul className="nav navbar-nav navbar-right">
          <li><button className="btn btn-info log">Log In</button></li>
          <li><button className="btn btn-danger log">Log out </button></li>
        </ul>
    );
  }
}

export default Nav;
