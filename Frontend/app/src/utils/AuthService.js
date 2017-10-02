import auth0 from 'auth0-js';

export default class AuthService {
  auth0 = new auth0.WebAuth({
    domain: 'gymbuddyios.auth0.com',
    clientID: 'aoBbzOkuq687XSK9lR2yOqKysVB6XmSJ',
    redirectUri: 'http://localhost:3000/courses',
    audience: 'https://gymbuddyios.auth0.com/userinfo',
    responseType: 'token id_token',
    scope: 'openid'
  });

  login() {
    this.auth0.authorize();
  }
}
