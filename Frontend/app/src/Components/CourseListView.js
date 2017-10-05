import React, { Component } from 'react';
import { Link } from 'react-router';
import Nav from './Nav';
import { getCourseData } from '../utils/api';


class CourseListView extends Component {

  constructor() {
    super()
    this.state = { courses: [] };
  }

  getCourseData() {
  getCourseData().then((courses) => {
    this.setState({ courses });
  });
}

componentDidMount() {
  this.getCourseData();
}

  render() {
    const { courses }  = this.state;
    console.log(courses);

    return (
      <div>
        <Nav auth={this.auth} {...this.props}  />
        <h3 className="text-center">Courses</h3>
        <hr/>

        { courses.map((course, index) => (
              <div className="col-sm-6" key={course.id}>
              {course.title}
              </div>
          ))}
          </div>
    );
  }
}

export default CourseListView;
