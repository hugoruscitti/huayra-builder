import Ember from 'ember';

export default Ember.Controller.extend({

  hasTask: function() {
    return (this.get('model.length') > 0);
  }.property('model.length'),


  statusWatch: function() {
    Ember.run.later(() => {

      console.log('tick');
      this.statusWatch();
    }, 1000)
  }.on('init'),

  actions: {

    update: function(user, repo) {

      $.ajax('/update').then((data) => {
        console.log(data);
      });

    }
  }
});
