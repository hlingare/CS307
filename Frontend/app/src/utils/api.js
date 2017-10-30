import axios from 'axios';

export {getCourseData,postUserData};

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
