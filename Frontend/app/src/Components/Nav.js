import React, { Component } from 'react';
import { Button } from 'react-bootstrap';

import history from '../history';

class Nav extends Component {
  logout() {
      this.props.auth.logout();
  }
  goTo() {
    history.replace('/profile');
  }

  render() {
    return (
        <ul className="nav navbar-nav navbar-right">

        <Button bsStyle="primary" className="btn-margin" onClick={this.logout.bind(this)}>
          Log Out
        </Button>

        <Button bsStyle="primary" className="btn-margin" onClick={this.goTo.bind(this)}>
          User Profile
        </Button>

        </ul>
    );
  }
}

export default Nav;
