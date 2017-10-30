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
