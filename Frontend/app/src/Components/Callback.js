<<<<<<< HEAD
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
=======
import { Component } from 'react';

class Callback extends Component {

  constructor() {
    super()
  }

  componentDidMount() {
    console.log(this.props);
  }

  render() {
    return null;
  }
}

export default Callback;
>>>>>>> 7a1d3ccb336b322fc03ebd46134d5d9af4150a20
