import logging
from settings import settings
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

logger=logging.getLogger(__name__)

class OutgoingSecurityCheck(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):

        try:
            response = await call_next(request)
        
            isApiKeyAllowed = settings.isOutgoingSecurityCheckEnabled == False or \
                ( (settings.isOutgoingSecurityCheckEnabled == True) and (settings.apikey_value != '') and (settings.apikey_value in settings.apikey_whitelist) )

            if ( isApiKeyAllowed == True ):
                return response                
            
            else:
                error_message = 'Servicio no disponible.'
                logger.error(error_message)
                return Response(content=error_message, status_code=503)
     
        except Exception as e500:
            exceptionJson = jsonable_encoder(e500)
            logger.error(exceptionJson, str(e500), exc_info=True)
            return Response(content='Lo sentimos, algo falló', status_code=500)

