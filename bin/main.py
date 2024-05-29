import zenoh
import logging
import warnings
import atexit
import json
import time
import keelson
from terminal_inputs import terminal_inputs
import api.compact as CompactApi

session = None
args = None



#####################################################
"""
# Processor stitching panorama image 
"""
if __name__ == "__main__":
    # Input arguments and configurations
    args = terminal_inputs()
    # Setup logger
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(name)s %(message)s", level=args.log_level
    )
    logging.captureWarnings(True)
    warnings.filterwarnings("once")

    ## Construct session
    logging.info("Opening Zenoh session...")
    conf = zenoh.Config()
    if args.connect is not None:
        conf.insert_json5(zenoh.config.CONNECT_KEY, json.dumps(args.connect))
    session = zenoh.open(conf)

    def _on_exit():
        session.close()

    atexit.register(_on_exit)
    logging.info(f"Zenoh session established: {session.info()}")




    #################################################
    # Setting up PUBLISHER

    # Camera panorama
    key_exp_lidar = keelson.construct_pub_sub_key(
        realm=args.realm,
        entity_id=args.entity_id,
        subject="compressed_image",  # Needs to be a supported subject
        source_id="panorama/" + args.output_id,
    )
    pub_camera_panorama = session.declare_publisher(
        key_exp_pub_camera_pano,
        priority=zenoh.Priority.INTERACTIVE_HIGH(),
        congestion_control=zenoh.CongestionControl.DROP(),
    )
    logging.info(f"Created publisher: {key_exp_pub_camera_pano}")


    #################################################
    # Setting up Querible

    # Camera panorama
    key_exp_query_camera_pano = keelson.construct_req_rep_key(
        realm=args.realm,
        entity_id=args.entity_id,
        responder_id="panorama",
        procedure="get_panorama",
    )
    query_camera_panorama = session.declare_queryable(
        key_exp_query_camera_pano,
        query_panorama
    )
    logging.info(f"Created queryable: {key_exp_query_camera_pano}")

    #################################################

    try:

        # TODO: SUBSCRIPTION initialization for panorama image creation
        if args.trigger_sub is not None:
            logging.info(f"Trigger Subscribing Key: {args.trigger_sub}")
            key_exp_sub_camera = keelson.construct_pub_sub_key(
                realm=args.realm,
                entity_id=args.entity_id,
                subject="compressed_image",  # Needs to be a supported subject
                source_id=args.trigger_sub,
            )

            # Declaring zenoh publisher
            sub_camera = session.declare_subscriber(
                key_exp_sub_camera, subscriber_camera_publisher
            )


    except KeyboardInterrupt:
        logging.info("Program ended due to user request (Ctrl-C)")
    except Exception as e:
        logging.error(f"Program ended due to error: {e}")

    # finally:
    #     logging.info("Closing Zenoh session...")
    #     session.close()
    #     logging.info("Zenoh session closed.")
