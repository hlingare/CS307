import React, { Component } from 'react';

var assert = require('assert');
var sinon = require('sinon');
var PassThrough = require('stream').PassThrough;
var http = require('http');
 
var api = require('../api.js');
 
describe('api', function() {
	beforeEach(function() {
		this.request = sinon.stub(http, 'request');
	});
 
	afterEach(function() {
		http.request.restore();
	});
 
 
	//We will place our tests cases here
 
});