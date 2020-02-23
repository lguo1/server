from flask import Flask, jsonify, request, send_from_directory, abort, render_template
from setup import db, app, Event, Proposal, Organizer, Subscription, Feedback, Login
@app.route('/event/')
def getAllEvents():
    events = db.session.query(Event)
    output = {}
    for event in events:
        output[event.id] = event.represent
    return jsonify(output)

@app.route('/organizer/')
def getAllOrganizer():
    organizers = db.session.query(Organizer)
    output = {}
    for organizer in organizers:
        output[organizer.id] = organizer.represent
    return jsonify(output)

@app.route('/organizer/<organizer_id>')
def getOrganizer(organizer_id):
    organizer = db.session.query(Organizer).filter_by(id = organizer_id).one()
    return jsonify(organizer.represent)

@app.route('/event/<event_id>')
def getEvent(event_id):
    event = db.session.query(event).filter_by(id = event_id).one()
    return jsonify(event.represent)

app.config['CLIENT_IMAGES'] = "./static/img"
@app.route('/img/<image_name>/')
def getImage(image_name):
    try:
        return send_from_directory(app.config['CLIENT_IMAGES'], filename = image_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)

@app.route('/help/')
def getHelp():
    return render_template('index.html')

@app.route('/propose/', methods = ["POST"])
def postProposal():
    proposal = Proposal(email = request.json['email'],
                        organizer = request.json['organizer'],
                        description = request.json['description'])
    db.session.add(proposal)
    db.session.commit()
    return "done"

@app.route('/feedback/', methods = ["POST"])
def postFeedback():
    feedback = Feedback(email = request.json['email'],
                        content = request.json['content'])
    db.session.add(feedback)
    db.session.commit()
    return "done"

@app.route('/login/', methods = ["POST"])
def postSubscription():
    login = Login(password = request.json['password'],
                        name = request.json['name'])
    db.session.add(login)
    db.session.commit()
    return "done"

@app.route('/subscribe/', methods = ["POST"])
def postLogin():
    subscription = Subscription(email = request.json['email'],
                                organizer = request.json['organizer'])
    db.session.add(subscription)
    db.session.commit()
    return "done"

@app.route('/admin/subscription/')
def getSubscription():
    output = {}
    organizers = db.session.query(Organizer)
    for organizer in organizers:
        subscriptions = organizer.subscriptions.group_by(Subscription.email).having(db.func.count(Subscription.email)%2 == 1)
        output[organizer.id] = [subscription.email for subscription in subscriptions]
    return jsonify(output)

@app.route('/admin/proposal/')
def getProposal():
    output = {}
    for proposal in db.session.query(Proposal):
        if proposal.organizer in output:
            output[proposal.organizer].append(proposal.description)
        else:
            output[proposal.organizer] = [proposal.description]
    return jsonify(output)

@app.route('/admin/event/')
def getEventByOrgainzer():
    output = {}
    organizers = db.session.query(Organizer)
    for organizer in organizers:
        events = organizer.events
        output[organizer.id] = [event.speaker for event in events]
    return jsonify(output)

@app.route('/admin/feedback/')
def getFeedback():
    output = {}
    for result in db.session.query(Feedback.email).distinct():
        email = tuple(result)[0]
        feedbacks = db.session.query(Feedback).filter_by(email = email)
        output[email] = [feedback.content for feedback in feedbacks]
    return jsonify(output)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5050)
