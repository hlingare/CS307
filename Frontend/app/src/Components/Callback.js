import { Component } from 'react';

class Callback extends Component {

  constructor() {
    super()
  }

  componentDidMount() {
    window.location.href = "/courses";
  }

  render() {
    return null;
  }
}

export default Callback;
