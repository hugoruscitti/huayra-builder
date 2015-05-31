import Ember from 'ember';

export function repoUser(params) {
  return params[0].split('/')[0];
}

export default Ember.HTMLBars.makeBoundHelper(repoUser);
