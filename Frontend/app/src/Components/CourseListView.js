import React, { Component } from 'react';
import { Link } from 'react-router';
import Nav from './Nav';
import '../styles/courseList.css';
import { getCourseData } from '../utils/api';
import history from '../history';
import Course from './Course';
import { Button } from 'react-bootstrap';
import SearchInput, {createFilter} from 'react-search-input';
const KEYS_TO_FILTERS = ['name']


class CourseListView extends Component {

  constructor() {
    super()
    this.state = {
      courses: [],
      searchTerm: ''
    };
    this.searchUpdated = this.searchUpdated.bind(this);
    this.sort = this.sort.bind(this);
  }


  getCourseData() {
  getCourseData().then((courses) => {
    this.setState({ courses });
  });
}

componentDidMount() {
  this.getCourseData();
}
searchUpdated (term) {
  this.setState({searchTerm: term})
}
sort() {
  const myData = [].concat(this.state.courses)
    .sort((a, b) => b.upvote - a.upvote)
    this.setState({courses: myData})

}

  render() {
    const { courses }  = this.state;
     const filteredCourses = courses.filter(createFilter(this.state.searchTerm, KEYS_TO_FILTERS))

    return (
    <div>
      <div className="container">
        <Nav auth={this.auth} {...this.props}  />
        <h3 className="text-center">Courses</h3>
          </div>
          <div className="list">
        <SearchInput className="search-input" onChange={this.searchUpdated} />
        <button><img src={require('./caret-arrow-up.png')} alt="sort ascending" onClick={this.sort} /></button>
        { filteredCourses.map((course, index) => (
              <div className="courseName" key={course.id}>
              <span>
                <Course
                  title={course.name}
                  score={course.score}
                >
                </Course>
              </span>
            </div>
          ))}
          </div>
          </div>
    );
  }
}

export default CourseListView;
