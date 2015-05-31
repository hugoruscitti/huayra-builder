import Ember from 'ember';

export function repoLink(params) {
  var string = "<a target='_blank' href='http://github.com/" + params + "/'>github</a>";
  return new Ember.Handlebars.SafeString(string);
}

export default Ember.HTMLBars.makeBoundHelper(repoLink);
