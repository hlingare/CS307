import axios from 'axios';

export {getCourseData,postUserData,postCourseData};

function getCourseData() {
  const url = `https://courserec.herokuapp.com/prereg`;
  return axios.get(url).then(response => response.data);
}
function postUserData(userIdAuth0,name) {
 const url = `https://courserec.herokuapp.com/showStudent`;
  axios.post(url, {
      userId: userIdAuth0,
      name: name
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});
}

function postCourseData(userIdAuth0,Coursename,Number1) {
 const url = `https://courserec.herokuapp.com/showCourse`;
  axios.post(url, {
      userId: userIdAuth0,
      course_name: Coursename,
      option: Number1 
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});
}
