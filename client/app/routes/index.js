import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {

    return new Ember.RSVP.Promise((resolve) => {

      Ember.RSVP.all([
        this.store.find('task'),
        $.get('/repos'),
      ]).then((data) => {
        resolve({
          task: data[0],
          repos: data[1].repos
        });
      });

    });
  }
});
