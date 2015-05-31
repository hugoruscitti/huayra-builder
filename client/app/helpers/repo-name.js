import Ember from 'ember';

export function repoName(params) {
  return params[0].split('/')[1];
}

export default Ember.HTMLBars.makeBoundHelper(repoName);
