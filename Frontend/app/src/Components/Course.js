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
  if (!this.state.disabledUpvote) {
    this.setState({
      disabledUpvote: true,
      disabledDownvote: false,
      votes: this.state.votes + 1
    });
  }
  }
  handleDownvoteClicked() {
  if (!this.state.disabledDownvote) {
    this.setState({
      disabledUpvote: false,
      disabledDownvote: true,
      votes: this.state.votes - 1
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
  componentDidUpdate() {
    postVote(this.props.title,this.state.votes);
  }

  render() {
    return(
      <div>
      <span onClick={() => this.listcourse(this.props.title)}>{this.props.title}</span>
      <span className="recommend">{this.props.score}</span>
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
