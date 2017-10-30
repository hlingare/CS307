<<<<<<< HEAD
import axios from 'axios';

export {getCourseData};


function getCourseData() {
  const url = `https://courserec.herokuapp.com/prereg`;
  return axios.get(url).then(response => response.data);
}

function getProfileData() {
	const url = `https://courserec.herokuapp.com/prereg`;
	  return axios.get(url).then(response => response.data);fffffff
}




=======
import axios from 'axios';

export {getCourseData,postUserData};

function getCourseData() {
  const url = `https://courserec.herokuapp.com/prereg`;
  return axios.get(url).then(response => response.data);
}
function postUserData(userIdAuth0) {
 const url = `https://courserec.herokuapp.com/prereg`;
  axios.post(url, {
    userId: userIdAuth0,
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});
}
>>>>>>> 7a1d3ccb336b322fc03ebd46134d5d9af4150a20
