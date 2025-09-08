# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
"""Schema for include.yaml configuration file.

.. literalinclude:: _spack_root/lib/spack/spack/schema/include.py
   :lines: 12-
"""
from typing import Any, Dict

#: Properties for inclusion in other schemas
properties: Dict[str, Any] = {
    "include": {
        "type": "array",
        "default": [],
        "additionalProperties": False,
        "description": "Include external configuration files to pull in configuration from "
        "other files/URLs for modular and reusable configurations",
        "items": {
            "anyOf": [
                {
                    "type": "object",
                    "description": "Advanced include entry with optional conditions and "
                    "remote file support",
                    "properties": {
                        "when": {
                            "type": "string",
                            "description": "Include this config only when the condition (as "
                            "Python code) evaluates to true",
                        },
                        "path": {
                            "type": "string",
                            "description": "Path to configuration file/directory (absolute, "
                            "relative, or URL). URLs must be raw file content (GitHub/GitLab "
                            "raw form). Supports file, ftp, http, https schemes and "
                            "Spack/environment variables",
                        },
                        "sha256": {
                            "type": "string",
                            "description": "Required SHA256 hash for remote URLs to verify "
                            "file integrity",
                        },
                        "optional": {
                            "type": "boolean",
                            "description": "If true, include only if path exists; if false "
                            "(default), path is required and missing files cause errors",
                        },
                    },
                    "required": ["path"],
                    "additionalProperties": False,
                },
                {
                    "type": "string",
                    "description": "Simple include entry specifying path to required "
                    "configuration file/directory",
                },
            ]
        },
    }
}

#: Full schema with metadata
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Spack include configuration file schema",
    "type": "object",
    "additionalProperties": False,
    "properties": properties,
}
