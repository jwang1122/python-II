from pymonad.either import Left, Right

authorized = True

def agentAuthorization(agent_id):
    if authorize(agent_id):
        response = {'status':'success', 'message':'Valid agent.', 'agent_id':'12345'}
        return Right(response)
    response = {'status':'failed', 'message':'Invalid agent.'}
    return Left(response)

def seatAvailability:
    if seatAvailable:
        response = {'status':'success', 'message':'Valid agent.', 'seats':['seat1','seat2','seat3']}
        return Right(response)
    response = {'status':'failed', 'message':'No seat available.', 'seats':[]}
    return Left(response)

def checkCustomerCredit:
    if seatAvailable:
        response = {'status':'success', 'message':'Valid agent.', 'seats':['seat1','seat2','seat3']}
        return Right(response)
    response = {'status':'failed', 'message':'No seat available.', 'seats':[]}
    return Left(response)

def paymentProcess:
    if seatAvailable:
        response = {'status':'success', 'message':'Valid agent.', 'seats':['seat1','seat2','seat3']}
        return Right(response)
    response = {'status':'failed', 'message':'No seat available.', 'seats':[]}
    return Left(response)

def issueTicket:
    if seatAvailable:
        response = {'status':'success', 'message':'Valid agent.', 'seats':['seat1','seat2','seat3']}
        return Right(response)
    response = {'status':'failed', 'message':'No seat available.', 'seats':[]}
    return Left(response)


