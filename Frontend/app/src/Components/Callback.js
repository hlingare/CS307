import { Component } from 'react';

class Callback extends Component {

  constructor() {
    super()
  }

  componentDidMount() {
    console.log(this.props);
    console.log(this.state,"gg");
  }

  render() {
    return null;
  }
}

export default Callback;