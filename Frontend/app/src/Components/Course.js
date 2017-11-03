import React,{ Component } from 'react';
import { Button } from 'react-bootstrap';
import history from '../history';
import { postVote,getVote } from '../utils/api';
import '../styles/CourseUpVoteDown.css';

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
      <label bsStyle="namelabel" className="namelabel" onClick={() => this.listcourse(this.props.title)}>{this.props.title}</label>
      <span className="recommend">{this.props.score}</span>
      <Button
          bsStyle="upvote" className="upvote"
          label="Upvote"
          disabled={this.state.disabledUpvote}
          onClick={this.handleUpvoteClicked}>
          +
      </Button>

      <Button
        bsStyle="downvote" className="downvote"
        label="Downvote"
        disabled={this.state.disabledDownvote}
        onClick={this.handleDownvoteClicked}>
        -
      </Button>

        <label>{this.state.votes}</label>
        </div>
    )
  }
}

export default Course;
