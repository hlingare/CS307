import React, { Component } from 'react';
import { Link } from 'react-router';
import Nav from './Nav';


class CourseListView extends Component {

  constructor() {
    super()
    this.state = { courses: ['Soc100'] };
  }


  render() {
    const { courses }  = this.state;

    return (
      <div>
        <Nav auth={this.auth} {...this.props}  />
        <h3 className="text-center">Courses</h3>
        <hr/>

        { courses.map((course, index) => (
              <div className="col-sm-6" key={index}>
              {course}
              </div>
          ))}
          </div>
    );
  }
}

export default CourseListView;
