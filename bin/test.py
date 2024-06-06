import api.compact as CompactApi

if __name__ == "__main__":

    receiver = CompactApi.Receiver(port=2115, host="10.10.30.1")
    (segments, frameNumbers, segmentCounters) = receiver.receiveSegments(200)
    receiver.closeConnection()