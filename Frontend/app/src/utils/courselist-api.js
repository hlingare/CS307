import axios from 'axios';

const BASE_URL = 'http://localhost:3000';

export {getCourseData};

function getCourseData() {
  const url = `${BASE_URL}/Backend/courses`;
  return axios.get(url).then(response => response.data);
}

