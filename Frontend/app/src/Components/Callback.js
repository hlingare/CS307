import { Component } from 'react';

class Callback extends Component {

  constructor() {
    super()
  }

  componentDidMount() {
    console.log(this.props);
    debugger;
    //window.location.href = "/courses";
  }

  render() {
    return null;
  }
}

export default Callback;
