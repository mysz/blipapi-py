<?php

/**
 * Blip! (http://blip.pl) communication library.
 *
 * @author Marcin Sztolcman <marcin /at/ urzenia /dot/ net>
 * @version 0.02.20
 * @version $Id$
 * @copyright Copyright (c) 2007, Marcin Sztolcman
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License v.2
 * @package blipapi
 */

/**
 * Blip! (http://blip.pl) communication library.
 *
 * @author Marcin Sztolcman <marcin /at/ urzenia /dot/ net>
 * @version 0.02.20
 * @version $Id$
 * @copyright Copyright (c) 2007, Marcin Sztolcman
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License v.2
 * @package blipapi
 */

if (!class_exists ('BlipApi_Movie')) {
    class BlipApi_Movie extends BlipApi_Abstract implements IBlipApi_Command {
        protected $_id;
        protected function __set_id ($value) {
            $this->_id = $this->__validate_offset ($value);
        }

        /**
        * Read movie attached to status/message/update
        *
        * Throws InvalidArgumentException when status ID is missing
        *
        * @access public
        * @return array parameters for BlipApi::__query
        */
        public function read () {
            if (!$this->_id) {
                throw new InvalidArgumentException ('Update ID is missing.', -1);
            }
            return array ("/updates/$this->_id/movie", 'get');
        }
    }
}

