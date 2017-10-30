<<<<<<< HEAD
import React, { Component } from 'react';
import { Button } from 'react-bootstrap';

import history from '../history';
<<<<<<< HEAD
import '../styles/nav.css';
=======
>>>>>>> c9d69db426ac4532f4d8edbc6797f95a7aad8196

class Nav extends Component {
  logout() {
      this.props.auth.logout();
  }
<<<<<<< HEAD
  goTo() {
    history.replace('/profile');
  }

  render() {
    return (
        <ul className="nav">

        <Button bsStyle="primary" className="btn-logout" onClick={this.logout.bind(this)}>
          Log Out
        </Button>

        <Button bsStyle="primary" className="btn-user" onClick={this.goTo.bind(this)}>
          User Profile
        </Button>

=======

  render() {
    return (
        <ul className="nav navbar-nav navbar-right">
        <Button
          bsStyle="primary"
          className="btn-margin"
          onClick={this.logout.bind(this)}
        >
          Log Out
        </Button>
>>>>>>> c9d69db426ac4532f4d8edbc6797f95a7aad8196
        </ul>
    );
  }
}

export default Nav;
=======
import React, { Component } from 'react';
import { Button } from 'react-bootstrap';

import history from '../history';
import '../styles/nav.css';

class Nav extends Component {
  logout() {
      this.props.auth.logout();
  }
  goTo() {
    history.push('/profile');
  }

  render() {
    return (
        <ul className="nav">

        <Button bsStyle="primary" className="btn-logout" onClick={this.logout.bind(this)}>
          Log Out
        </Button>

        <Button bsStyle="primary" className="btn-user" onClick={this.goTo.bind(this)}>
          User Profile
        </Button>

        </ul>
    );
  }
}

export default Nav;
>>>>>>> 7a1d3ccb336b322fc03ebd46134d5d9af4150a20
