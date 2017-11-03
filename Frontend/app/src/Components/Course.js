import React,{ Component } from 'react';
import { Button } from 'react-bootstrap';
import history from '../history';
import { postVote,getVote } from '../utils/api';

class Course extends Component {

  constructor() {
    super()
    this.state = {
      disabledUpvote: false,
      disabledDownvote: false,
      votes: 0
    };
    this.handleUpvoteClicked = this.handleUpvoteClicked.bind(this);
    this.handleDownvoteClicked = this.handleDownvoteClicked.bind(this);
  }

  handleUpvoteClicked() {
  console.log(this.state.votes);
  if (!this.state.disabledUpvote) {
    this.setState({
      disabledUpvote: true,
      disabledDownvote: false,
      votes: 1 + this.state.votes
    });
    console.log(this.state.votes);
  }
  }
  handleDownvoteClicked() {
  if (!this.state.disabledDownvote) {
    this.setState({
      disabledUpvote: false,
      disabledDownvote: true,
      votes: 1 - this.state.votes
    });
  }
  }

  listcourse(title) {
   history.push({
    pathname: '/listcourse',
    state: { detail: title }
   })
    }

  componentDidMount() {
    getVote(this.props.title).then((courses) => {
      this.setState({ votes: courses.result.upvote });
    });
  }
  componentWillUnmount() {
    postVote(this.props.title,this.state.votes);
  }

  render() {
    return(
      <div>
      <span onClick={() => this.listcourse(this.props.title)}>{this.props.title}</span>
      <span className="recommend">{'RECOMMENDED'}</span>
        <Button
          label="Upvote"
          disabled={this.state.disabledUpvote}
          onClick={this.handleUpvoteClicked} >
      </Button>
      <Button
        label="Downvote"
        disabled={this.state.disabledDownvote}
        onClick={this.handleDownvoteClicked}>
        </Button>
        <span>{this.state.votes}</span>
        </div>

    )
  }
}

export default Course;
