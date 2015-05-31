import DS from 'ember-data';

export default DS.Model.extend({
  user: DS.attr('string'),
  repo: DS.attr('string'),
  status: DS.attr('string'),
  time: DS.attr('date')
});
