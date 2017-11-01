import axios from 'axios';

export {getCourseData,getCourse,getProfileData,postUserData,postCourseData};

function getCourseData() {
  const url = `https://courserec.herokuapp.com/prereg`;
  return axios.get(url).then(response => response.data);
}

function getCourse() {
	const url = `https://courserec.herokuapp.com/getCourse`;
	return axios.get(url).then(response => response.data);
}

function getProfileData(userIdAuth0) {
	const url = `https://courserec.herokuapp.com/getUserName/` + userIdAuth0;
	return axios.get(url).then(response => response.data);
}

function postUserData(userIdAuth0,courseName) {
 const url = `https://courserec.herokuapp.com/showStudent/` + userIdAuth0 + `,` + courseName;

  axios.post(url, {
      userId: userIdAuth0,
      cname: courseName
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});
}

//11 = bad, 12 = okay, 13 = good
function postCourseData(userIdAuth0,Coursename,courseOption) {
 const url = `https://courserec.herokuapp.com/showCourse`;
  axios.post(url, {
      userId: userIdAuth0,
      course_name: Coursename,
      option: courseOption
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});
}
