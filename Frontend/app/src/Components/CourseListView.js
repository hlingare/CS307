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
    console.log(courses);
     const filteredCourses = courses.filter(createFilter(this.state.searchTerm, KEYS_TO_FILTERS))

    return (
    <div>
      <div className="container">
        <Nav auth={this.auth} {...this.props}  />
        <h3 className="text-center">Courses</h3>
          </div>
          <span className="header">
          <SearchInput className="search-input" onChange={this.searchUpdated} />
            <button className="button"><img src={require('./caret-arrow-up.png')} alt="sort ascending" onClick={this.sort} /></button>
            </span>
            <div class="tbl-header">
      <table cellpadding="0" cellspacing="0" border="0">
        <thead>
          <tr>
            <th>Course Name</th>
            <th>Vote</th>
            <th>vote Score</th>
            <th>Recommendation Score</th>
          </tr>
        </thead>
      </table>
    </div>
    <div class="tbl-content">
  <table cellpadding="0" cellspacing="0" border="0">
    <tbody>
        { filteredCourses.map((course, index) => (
              <tr key={course.id}>
                <td>
                <Course
                  title={course.name}
                  score={course.score}
                >
                </Course>
                </td>
                </tr>
          ))}
        </tbody>
      </table>
          </div>
            </div>
    );
  }
}

export default CourseListView;
