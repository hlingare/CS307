import React, { Component } from 'react';
import { Button } from 'react-bootstrap';

import history from '../history';

class Nav extends Component {
  logout() {
      this.props.auth.logout();
  }

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
        </ul>
    );
  }
}

export default Nav;
