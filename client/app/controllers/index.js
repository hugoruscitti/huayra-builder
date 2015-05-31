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
    clone: function(user, repo) {
      $.ajax('/clone/' + user + '/' + repo).then((data) => {
        this.store.createRecord('task', {
          user: user,
          repo: repo,
          status: data.status_url,
        });

      });
    }
  }
});
