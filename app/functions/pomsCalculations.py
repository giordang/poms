from app import db
from app.models import User, Poms
from flask_login import current_user
from datetime import datetime, timedelta
import pandas as pd
import matplotlib
import sqlite3


def pomsCalculator(form):
    #get data for each item
    #calculate summary scores
    #add individual and summary data to db

    allFields = ['tense', 'angry', 'wornOut', 'unhappy', 'proud', 'lively', 'confused', 'sad', 'active', 'onEdge', 'grouchy', 'ashamed', 'energetic', 'hopeless', 'uneasy', 'restless', 'unableToConcentrate', 'fatigued', 'competent', 'annoyed', 'discouraged', 'resentful', 'nervous', 'miserable', 'confident', 'bitter', 'exhausted', 'anxious', 'helpless', 'weary', 'satisfied', 'bewildered', 'furious', 'fullOfPep', 'worthless', 'forgetful', 'vigorous', 'uncertainAboutThings', 'bushed', 'embarrassed']
    ten = ['tense', 'onEdge', 'uneasy', 'restless', 'nervous', 'anxious']
    ang = ['angry', 'grouchy', 'annoyed', 'resentful', 'bitter', 'furious']
    fat = ['wornOut', 'fatigued', 'exhausted', 'weary', 'bushed']
    dep = ['unhappy', 'sad', 'hopeless', 'discouraged', 'miserable', 'helpless', 'worthless']
    era = ['proud', 'ashamded', 'competent', 'confident', 'satisfied', 'embarrassed']
    vig = ['lively', 'active', 'energetic', 'fullOfPep', 'vigorous']
    con = ['confused', 'unableToConcentrate', 'bewildered', 'forgetful', 'uncertainAboutThings']

    tenSum = 0
    angSum = 0
    fatSum = 0
    depSum = 0
    eraSum = 0
    vigSum = 0
    conSum = 0
    tmdSum = 0

    for field in form:
        if field.name in allFields:
            fieldName = field.name
            fieldData = field.data - 100
            tmdSum = tmdSum + fieldData
            if fieldName in ten:
                tenSum = tenSum + fieldData
            if fieldName in ang:
                angSum = angSum + fieldData
            if fieldName in fat:
                fatSum = fatSum + fieldData
            if fieldName in dep:
                depSum = depSum + fieldData
            if fieldName in era:
                eraSum = eraSum + fieldData
            if fieldName in vig:
                vigSum = vigSum + fieldData
            if fieldName in con:
                conSum = conSum + fieldData

    tmdSum = tenSum + depSum + angSum + fatSum + conSum - vigSum - eraSum

    item = Poms(
        tense = form.tense.data - 100,
        angry = form.tense.data - 100,
        wornOut = form.tense.data - 100,
        unhappy = form.tense.data - 100,
        proud = form.tense.data - 100,
        lively = form.tense.data - 100,
        confused = form.tense.data - 100,
        sad = form.tense.data - 100,
        active = form.tense.data - 100,
        onEdge = form.tense.data - 100,
        grouchy = form.tense.data - 100,
        ashamed = form.tense.data - 100,
        energetic = form.tense.data - 100,
        hopeless = form.tense.data - 100,
        uneasy = form.tense.data - 100,
        restless = form.tense.data - 100,
        unableToConcentrate = form.tense.data - 100,
        fatigued = form.tense.data - 100,
        competent = form.tense.data - 100,
        annoyed = form.tense.data - 100,
        discouraged = form.tense.data - 100,
        resentful = form.tense.data - 100,
        nervous = form.tense.data - 100,
        miserable = form.tense.data - 100,
        confident = form.tense.data - 100,
        bitter = form.tense.data - 100,
        exhausted = form.tense.data - 100,
        anxious = form.tense.data - 100,
        helpless = form.tense.data - 100,
        weary = form.tense.data - 100,
        satisfied = form.tense.data - 100,
        bewildered = form.tense.data - 100,
        furious = form.tense.data - 100,
        fullOfPep = form.tense.data - 100,
        worthless = form.tense.data - 100,
        forgetful = form.tense.data - 100,
        vigorous = form.tense.data - 100,
        uncertainAboutThings = form.tense.data - 100,
        bushed = form.tense.data - 100,
        embarrassed = form.tense.data - 100,
        tenSum = tenSum,
        angSum = angSum,
        fatSum = fatSum,
        depSum = depSum,
        eraSum = eraSum,
        vigSum = vigSum,
        conSum = conSum,
        tmdSum = tmdSum,
        user_id = current_user.id
    )

    db.session.add(item)
    db.session.commit()


def pomsGrapher():
    currentTime = datetime.utcnow()
    yesterday = currentTime - timedelta(hours=1)
    yesterdayPoms = Poms.query.filter(Poms.user_id == current_user.id).filter(Poms.timestamp > yesterday)

    con = db.engine.connect().connection
    df = pd.read_sql_query(str(yesterdayPoms), con, params=[current_user.id, yesterday])
    #df.to_csv('lala.csv')

    """
    df['date'] = df['poms_timestamp'].astype('datetime64').dt.date
    dfGroup = df.groupby(['date', 'poms_user_id']).mean().reset_index()

    if len(dfGroup) == 1:
        fig = dfGroup.plot.bar(x='date', y='poms_tmdSum', rot=60).get_figure()
        fig.tight_layout()
    else:
        delta = pd.Timedelta(days=7)
        lims = [dfGroup['date'] - delta, dfGroup['date']]
        fig = dfGroup.plot(x='date',y='poms_tmdSum', style='.-', rot=60,xlim=lims).get_figure()
        fig.tight_layout()

    fig.savefig('app/graphs/week.png')
    """
    print(df)
    
    
    con.close()

